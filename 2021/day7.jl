using Statistics

function main()
    input_str = open(f->read(f, String), "input_day7.txt")
    crabs = map(s -> parse(Int, s), split(input_str, ","))
    pos = round(median(crabs))
    println("Crabs will move to position: $pos")

    totalcost = 0
    for crab in crabs
        totalcost += abs(crab-pos)
    end
    println("Answer 1: $totalcost")
end

main()
