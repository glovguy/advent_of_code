using Statistics

int(x) = floor(Int, x)

mutable struct Champ
    val::Int
    cost::Int
end

function main()
    input_str = open(f->read(f, String), "input_day7.txt")
    crabs = map(s -> parse(Int, s), split(input_str, ","))
    # not sure if it was just a fluke that this was the median
    pos = int(round(median(crabs)))
    println("Crabs will move to position: $pos")

    totalcost = 0
    for crab in crabs
        totalcost += abs(crab-pos)
    end
    println("Answer 1: $totalcost")

    ## Part 2

    # calculate this once upfront
    maxdist = maximum(crabs)
    costfordist = fill(1, maxdist)
    for i in 2:maxdist
        costfordist[i] = costfordist[i-1] + i
    end
    # 1,3,6,10,15,21
    # 1,2,3, 4, 5, 6
    function cost(dist::Int, costfordist::Array)
        return (dist == 0) ? 0 : costfordist[dist]
    end
    cost(d::Int) = cost(d::Int, costfordist) # Julia is so cool
    
    champ = nothing
    costsforspots = fill(0, maxdist)
    # O(n^2), but ran fast enough on my machine
    for i in 1:maxdist
        total = 0
        for crab in crabs
            total += cost(int(abs(crab-i)))
        end
        costsforspots[i] = total

        if isnothing(champ) || total < champ.cost
            champ = Champ(i, total)
        end
    end

    pos2 = champ.val
    totalcost2 = champ.cost
    println("Crabs will instead move to position: $pos2")
    println("Answer 2: $totalcost2")
end

main()
