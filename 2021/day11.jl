
function main()
    input_str = open(f->read(f, String), "input_day11.txt")
    octos = hcat(map(c -> parse.(Int, collect(c)), split(input_str, "\n"))...)

    neighborindices = filter(x -> Tuple(x) != (0,0), CartesianIndex(-1,-1):CartesianIndex(1,1))
    function isneighborvalid(x::CartesianIndex, w, h)
        return x[1] >= 1 &&
            x[1] <= w &&
            x[2] >= 1 &&
            x[2] <= h
    end
    isneighborvalid(x) = isneighborvalid(x, size(octos)[1], size(octos)[2])
    validneighbors(i) = filter(isneighborvalid, [i] .+ copy(neighborindices))

    flashCount = 0
    step = 1
    ans2 = nothing
    flashingOctos = Dict()

    function excite(i)
        octos[i] += 1
        if !haskey(flashingOctos, i) && octos[i] > 9
            flashingOctos[i] = true
            foreach(excite, validneighbors(i))
        end
    end

    function tick()
        foreach(excite, CartesianIndices(octos))
        flashCount += length(flashingOctos)

        if isnothing(ans2) && length(keys(flashingOctos)) == length(octos)
            println("Answer 2: ", step)
            ans2 = step
        end

        for key in keys(flashingOctos)
            octos[key] = 0
            delete!(flashingOctos, key)
        end

        step += 1
    end

    for _ in 1:100
        tick()
    end

    println("Answer 1: ", flashCount)
    
    for _ in 1:1000
        if !isnothing(ans2)
            return
        end
        tick()
    end
end

main()
