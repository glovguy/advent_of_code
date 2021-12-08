struct Coord
    x::Int
    y::Int
end
struct Vents
    from::Vector{Coord}
    to::Vector{Coord}
end


function main()
    input_str = open(f->read(f, String), "input_day5.txt")
    lines = split(input_str, "\n")
    point_pair_strs = map(l -> split(l, " -> "), lines)
    point_pairs = map.(p -> parse.(Int,split(p, ",")), point_pair_strs)
    point_pairs = filter(p -> p[1][1] == p[2][1] || p[1][2] == p[2][2], point_pairs)
    
    countdict = Dict()
    count = 0

    for vent in point_pairs
        xrange = (vent[1][1] <= vent[2][1]) ? (vent[1][1]:vent[2][1]) : (vent[2][1]:vent[1][1])
        for i in xrange
            yrange = (vent[1][2] <= vent[2][2]) ? (vent[1][2]:vent[2][2]) : (vent[2][2]:vent[1][2])
            for j in yrange
                key = "$i:$j"
                countdict[key] = get(countdict, key, 0) + 1
                if countdict[key] == 2
                    count += 1
                end
            end
        end
    end
    
    println(count)
end

main()
