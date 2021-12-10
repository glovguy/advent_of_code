
function main()
    input_str = open(f->read(f, String), "input_day8.txt")
    lines = split(input_str, "\n")
    split_lines = map(l -> split(l, " | "), lines)
    lines_with_wires = map(l -> [split(l[1], " "),split(l[2], " ")], split_lines)

    count = 0
    for wire_line in lines_with_wires
        # wire_inputs = wire_line[2]
        # println(wire_line)
        for wire_input in wire_line[2]
            len = length(wire_input)
            if len == 2 || len == 4 || len == 3 || len == 7
                # println(wire_input)
                count += 1
            end
        end
    end
    println(count)
end

main()
