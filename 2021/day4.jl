mutable struct Board
    lookupdict::Dict
    rowtotals::Array{Int}
    coltotals::Array{Int}
    iswinner::Bool
end
Board() = Board(Dict(), Array{Int}(undef, 5), Array{Int}(undef, 5), false)

mutable struct Coord
    row::Int
    col::Int
    seen::Bool
end
Coord(x, y) = Coord(x, y, false)

function iswinner(board::Board)
    for tot in board.coltotals
        if tot >= 5
            return true
        end
    end
    for tot in board.rowtotals
        if tot >= 5
            return true
        end
    end
    return false
end

function score(num::Int, board::Board)
    sum = 0
    for (key, value) in board.lookupdict
        
        if !value.seen
            sum += key
        end
    end
    return sum*num
end

function main()
    input_str = open(f->read(f, String), "input_day4.txt")
    chunks = split(input_str, "\n\n")
    
    drawn_numbers = map(c -> parse(Int,c), split(chunks[1], ","))
    boards = Array{Board, 1}(undef, length(chunks)-1)
    for i in 1:length(boards)
        boards[i] = Board()
    end

    winner_count = 0

    # populate lookupdict
    for b in 1:length(boards)
        board = boards[b]
        
        rows = split(chunks[b+1], "\n")
        for i in 1:5
            # the filter isempty is to handle multiple spaces
            cells = filter(c -> !isempty(c), split(rows[i], " ")) 
            for j in 1:length(cells)
                value = parse(Int, cells[j])
                board.lookupdict[value] = Coord(i,j)
            end
        end
    end
    
    for num in drawn_numbers
        for board in boards
            loc = get(board.lookupdict, num, nothing)
            if !isnothing(loc)
                board.rowtotals[loc.row] += 1
                board.coltotals[loc.col] += 1
                board.lookupdict[num].seen = true
                if iswinner(board)
                    if winner_count == 0
                        ans = score(num, board)
                        println("Answer 1: $ans")
                    end
                    if !board.iswinner
                        winner_count += 1
                    end
                    board.iswinner = true
                    if winner_count == length(boards)
                        ans = score(num, board)
                        println("Answer 2: $ans")
                        return
                    end
                end
            end
        end
    end
end

main()
