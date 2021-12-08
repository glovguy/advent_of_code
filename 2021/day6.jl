function main()
    input_str = open(f->read(f, String), "input_day6.txt")
    fishes = map(s -> parse(Int, s), split(input_str, ","))

    fishtank = fill(0, 10) # { [index: age] => count }
    # problem assumes a zero-indexed array is being used
    for fishAge in fishes
        fishtank[fishAge+1] = fishtank[fishAge+1] + 1
    end

    function tick(tank) 
        newfish = tank[1]
        for i in 1:9
            tank[i] = tank[i+1]
        end
        tank[7] = tank[7] + newfish
        tank[9] = tank[9] + newfish
    end

    for _ in 1:80
        tick(fishtank)
    end
    ans1 = sum(fishtank)

    remaining = 256-80
    for _ in 1:remaining
        tick(fishtank)
    end
    ans2 = sum(fishtank)

    println("Answer 1: $ans1")
    println("Answer 2: $ans2")
end

main()
