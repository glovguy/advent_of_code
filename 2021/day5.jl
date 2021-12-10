struct Coord
    x::Int
    y::Int
end
Coord(arr) = Coord(parse(Int, arr[1]), parse(Int, arr[2]))

struct Vent
    from::Coord
    to::Coord
end
Vent(pair) = Vent(pair[1], pair[2])
function ishorizontalorvetical(vent::Vent) 
    return vent.from.x == vent.to.x || vent.from.y == vent.to.y
end
minlength(vent::Vent) = max(abs(vent.from.x-vent.to.x)+1, abs(vent.from.y-vent.to.y)+1)
function xrange(vent::Vent)
    if vent.from.x == vent.to.x
        return fill(vent.from.x, minlength(vent))
    end
    return (vent.from.x < vent.to.x) ? (vent.from.x:vent.to.x) : reverse(vent.to.x:vent.from.x)
end
function yrange(vent::Vent)
    if vent.from.y == vent.to.y
        return fill(vent.from.y, minlength(vent))
    end
    return (vent.from.y < vent.to.y) ? (vent.from.y:vent.to.y) : reverse(vent.to.y:vent.from.y)
end

function main()
    input_str = open(f->read(f, String), "input_day5.txt")
    lines = split(input_str, "\n")
    point_pair_strs = map(l -> split(l, " -> "), lines)
    point_pairs = map.(p -> Coord(split(p, ",")), point_pair_strs)
    vents = map(pair -> Vent(pair), point_pairs)
    
    countdict1 = Dict()
    count1 = 0
    countdict2 = Dict()
    count2 = 0

    for vent in vents
        hv = ishorizontalorvetical(vent)
        xr = xrange(vent)
        yr = yrange(vent)
        
        for i in 1:minlength(vent)
            x = xr[i]
            y = yr[i]
            key = [x,y]
            
            countdict2[key] = get(countdict2, key, 0) + 1
            if countdict2[key] == 2
                count2 += 1
            end
            if !hv
                continue
            end
            countdict1[key] = get(countdict1, key, 0) + 1
            if countdict1[key] == 2
                count1 += 1
            end
        end
    end
    
    # for i in 0:9
    #     for j in 0:9
    #         chr = get(countdict2, [j,i], ".")
    #         print(chr, "")
    #     end
    #     println("")
    # end
    # println("\n---\n")

    """
    1.1....11.
    .111...2..
    ..2.1.111.
    ...1.2.2..
    .112313211
    ...1.2....
    ..1...1...
    .1.....1..
    1.......1.
    222111....
"""

    # for i in 0:10
    #     for j in 0:10
    #         chr = get(countdict1, [j,i], ".")
    #         print(chr, "")
    #     end
    #     println("")
    # end
    
    println("Answer 1: $count1")
    println("Answer 2: $count2")
end

main()
