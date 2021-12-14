
function main()
    input_str = open(f->read(f, String), "input_day3.txt")
    measurements = split(input_str, "\n")

    w = length(measurements[1])
    h = length(measurements)
    counts = fill(0, w)

    for measurement in measurements
        for i in 1:w
            if measurement[i] == '1'
                counts[i] += 1
            end
        end
    end

    gamma_str = ""
    eps_str = ""
    for c in counts
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
    ans1 = gamma*epsilon
    println("Answer 1: $ans1")

    oxy_measurements = copy(measurements)
    oxy = nothing
    co2_measurements = copy(measurements)
    co2 = nothing

    function countsat(arr::Array, i)
        count = 0
        for item in arr
            if item[i] == '1'
                count += 1
            end
        end

        return count
    end

    for i in 1:w
        if isnothing(oxy)
            count = countsat(oxy_measurements, i)
            mcd_oxy = (count >= length(oxy_measurements)/2) ? 1 : 0
            oxy_measurements = filter(m -> parse(Int, m[i]) == mcd_oxy, oxy_measurements)
            
            if length(oxy_measurements) == 1
                oxy = parse(Int, oxy_measurements[1], base=2)
            end
        end

        if isnothing(co2)
            count = countsat(co2_measurements, i)
            mcd_co2 = (count >= length(co2_measurements)/2) ? 0 : 1
            co2_measurements = filter(m -> parse(Int, m[i]) == mcd_co2, co2_measurements)
            
            if length(co2_measurements) == 1
                co2 = parse(Int, co2_measurements[1], base=2)
            end
        end
    end

    println("oxy: $oxy, co2: $co2")
    ans2 = oxy*co2
    println("Answer 2: $ans2")

end

main()
