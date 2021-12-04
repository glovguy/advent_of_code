
function main()
    input_str = open(f->read(f, String), "input_day2.txt")
    movements = split(input_str, "\n")

    posx = 0
    depth = 0


    for movement in movements
        direction, value_str = split(movement, " ")
        value = parse(Int64, value_str)
        # println(direction)
        # println(value)
        if direction == "up"
            depth -= value
        elseif direction == "down"
            depth += value
        elseif direction == "forward"
            posx += value
        end
    end

    println("Position: $posx, depth: $depth")
    ans = posx * depth
    println("Problem 1 answer: $ans")
end

main()

function main2()
end

main2()