function main()
    input_str = open(f->read(f, String), "input_day1.txt")
    measurements = map(m -> parse(Int64, m), split(input_str, "\n"))
    count = 0

    previous_measurement = nothing
    for measurement in measurements
        if !isnothing(previous_measurement) && measurement > previous_measurement
            count += 1
        end
        previous_measurement = measurement
    end

    return count
end
ans1 = main()
println("First part: $ans1")

function main2()
    input_str = open(f->read(f, String), "input_day1.txt")
    measurements = map(m -> parse(Int64, m), split(input_str, "\n"))
    left_window = measurements[1] + measurements[2] + measurements[3]
    right_window = measurements[2] + measurements[3] + measurements[4]
    count = 0

    previous_measurement = nothing
    for i in range(5, length(measurements)+1, step=1)
        
        if right_window > left_window
            count += 1
        end

        left_window -= measurements[i-4]
        left_window += measurements[i-1]
        
        right_window -= measurements[i-3]
        if i <= length(measurements)
            right_window += measurements[i]
        end
    end

    return count
end

ans2 = main2()
println("Second part: $ans2")
