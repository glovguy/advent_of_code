using LinearAlgebra

function main()
    input_str = open(f->read(f, String), "input_day13.txt")
    points_str, folds_str = split(input_str, "\n\n")
    points = map(p -> map(x -> 1+parse(Int, x), split(p, ",")), split(points_str, "\n"))
    folds = split(folds_str, "\n")
    
    x_values = map(p -> p[1], points)
    y_values = map(p -> p[2], points)

    paper = fill(false, (max(x_values...), max(y_values...)))
    for point in points
        paper[point...] = true
    end

    function iscoordvalid(x::CartesianIndex, s)
        return x[1] >= 1 &&
            x[1] <= s[1] &&
            x[2] >= 1 &&
            x[2] <= s[2]
    end
    iscoordvalid(x) = iscoordvalid(x, size(paper))

    function foldy(val)
        for x in 1:size(paper)[1]
            for y in (val+1):size(paper)[2]
                from = CartesianIndex(x,y)
                to = CartesianIndex(x,val+val-y)
                
                if !iscoordvalid(from) || !iscoordvalid(to)
                    continue
                end
                if paper[from]
                    paper[to] = paper[from]
                    paper[from] = false
                end
            end
        end
        paper = paper[1:end, 1:val]
    end

    function foldx(val)
        for x in (val+1):size(paper)[1]
            for y in 1:size(paper)[2]
                from = CartesianIndex(x,y)
                to = CartesianIndex(val+val-x,y)
                
                if !iscoordvalid(from) || !iscoordvalid(to)
                    continue
                end
                if paper[from]
                    paper[to] = paper[from]
                    paper[from] = false
                end
            end
        end
        paper = paper[1:val, 1:end]
    end

    function foldxy(fold)
        dir, val_str = split(fold, "=")
        val = parse(Int, val_str)+1 # input is 0-indexed :eyeroll:
        (dir == "fold along y") ? foldy(val) : foldx(val)
    end

    function pretty(paper)
        out = []
        for row in eachcol(paper)
            for c in row
                if c == true
                    push!(out, "#")
                else
                    push!(out, ".")
                end
            end
            push!(out, "\n")
        end
        return join(out, "")
    end

    for fold in folds[1:1]
        foldxy(fold)
    end
    println(sum(paper))

    for fold in folds[2:length(folds)]
        foldxy(fold)
    end

    function resize!(paper)
        mx = 0
        my = 0
        for i in CartesianIndices(paper)
            if paper[i] && i[1] > mx
                mx = i[1]
            end
            if paper[i] && i[2] > my
                my = i[2]
            end
        end
        paper = paper[1:mx,1:my]
    end

    println(pretty(paper))
end

main()
