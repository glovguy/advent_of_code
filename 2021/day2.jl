
function main()
    input_str = open(f->read(f, String), "input_day2.txt")
    movements = split(input_str, "\n")

    posx = 0
    depth = 0

    for movement in movements
        direction, value_str = split(movement, " ")
        value = parse(Int64, value_str)
        if direction == "up"
            depth -= value
        elseif direction == "down"
            depth += value
        elseif direction == "forward"
            posx += value
        end
    end

    println("Position: $posx, depth: $depth")
    ans1 = posx * depth
    println("Problem 1 answer: $ans1")

    posx = 0
    depth = 0
    aim = 0

    for movement in movements
        direction, value_str = split(movement, " ")
        value = parse(Int64, value_str)
        if direction == "up"
            aim -= value
        elseif direction == "down"
            aim += value
        elseif direction == "forward"
            posx += value
            depth += aim*value
        end
    end

    println("Position: $posx, depth: $depth")
    ans2 = posx * depth
    println("Problem 2 answer: $ans2")
end

main()
