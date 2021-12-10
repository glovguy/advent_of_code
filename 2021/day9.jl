
function main()
    input_str = open(f->read(f, String), "input_day9.txt")
    points = hcat(map(c -> parse.(Int, collect(c)), split(input_str, "\n"))...)

    neighborindices = [CartesianIndex(0,-1),CartesianIndex(-1,0),CartesianIndex(0,1),CartesianIndex(1,0)]

    function isneighborvalid(x::CartesianIndex, w, h)
        return x[1] >= 1 &&
            x[1] <= w &&
            x[2] >= 1 &&
            x[2] <= h
    end
    isneighborvalid(x) = isneighborvalid(x, size(points)[1], size(points)[2])
    validneighbors(i) = filter(isneighborvalid, [i] .+ copy(neighborindices))

    risksum = 0
    lowest_points = Array{CartesianIndex, 1}()
    for i in CartesianIndices(points)
        if isnothing(findfirst(el -> points[el] < points[i], validneighbors(i)))
            risksum += points[i] + 1
            push!(lowest_points, i)
        end
    end

    println("Answer 1: $risksum")

    basins = Array{Int, 1}()
    basin = 0

    function fillbasin(i)
        if points[i] == 9 || points[i] == -1
            return
        end
        
        basin += 1
        points[i] = -1
        for n in validneighbors(i)
            fillbasin(n)
        end
    end

    for i in lowest_points
        if points[i] != 9
            basin = 0
            fillbasin(i)
            push!(basins, copy(basin))
        end
    end
    # display(points)
    ans2 = reduce(*, sort(basins, rev=true)[1:3])
    println("ans2: $ans2")
end

main()
