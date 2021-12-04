
function main()
    input_str = open(f->read(f, String), "input_day3.txt")
    measurements = split(input_str, "\n")

    w = length(measurements[1])
    h = length(measurements)
    counts = fill(0, w)

    for measurement in measurements
        for i in range(1, w, step=1)
            if measurement[i] == '1'
                counts[i] += 1
            end
        end
    end

    gamma_str = ""
    eps_str = ""
    for c in counts
        # println(c)
        if c > h/2
            gamma_str *= "1"
            eps_str *= "0"
        else
            gamma_str *= "0"
            eps_str *= "1"
        end
    end
    
    gamma = parse(Int, gamma_str, base=2)
    epsilon = parse(Int, eps_str, base=2)
    println("gamma binary: $gamma_str, epsilon binary: $eps_str")
    println("gamma: $gamma, epsilon: $epsilon")
    ans = gamma*epsilon
    println("Answer: $ans")
end

main()
