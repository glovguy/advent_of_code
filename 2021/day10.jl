
function main()
    input_str = open(f->read(f, String), "input_day10.txt")
    lines = split(input_str, "\n")


    lookupdict = Dict('[' => ']', '(' => ')', '{' => '}', '<' => '>')
    scoredict = Dict(')' => 3, ']' => 57, '}' => 1197, '>' => 25137)

    function errorscore(line)
        stack = Array{Char,1}()
        for char in line
            if length(stack) > 0 && char == last(stack)
                pop!(stack)
                continue
            end
            nxt = get(lookupdict, char, nothing)
            if !isnothing(nxt)
                push!(stack, nxt)
                continue
            end
            
            return scoredict[char]
        end
        return 0
    end

    totalerrorscore = 0
    
    for line in lines
        totalerrorscore += errorscore(line)
    end
    println("Answer 1: ", totalerrorscore)

    autocompletescoredict = Dict(')' => 1, ']' => 2, '}' => 3, '>' => 4)

    function autocompletescore(line)
        stack = Array{Char,1}()
        
        for char in line
            if length(stack) > 0 && char == last(stack)
                pop!(stack)
                continue
            end
            nxt = get(lookupdict, char, nothing)
            if !isnothing(nxt)
                push!(stack, nxt)
                continue
            end
            
            return nothing
        end

        score = 0
        for c in reverse(stack)
            val = autocompletescoredict[c]
            score = (score * 5) + val
        end

        return score
    end

    scores = filter(n -> !isnothing(n), map(autocompletescore, lines))
    mid = floor(Int, (length(scores)/2)+0.5)
    println(sort(scores)[mid])
end

main()
