
function main(input_str)
  elves = split(input_str, "\n\n")

  cals = map(calories, elves)
  cals = sort(cals)

  return cals
end

function calories(elf)
  return sum(map(m -> parse(Int64, m), split(elf, "\n")))
end

test_input = "1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"

input_str = open(f->read(f, String), "inputs/day1_input.txt")

cals = main(input_str)
println("Answer 1: ", cals[length(cals)])
println("Answer 2: ", sum(cals[length(cals)-2:length(cals)]))
