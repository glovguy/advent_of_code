require_relative 'triangle'

impossible = 0
possible = 0
file = File.open("input_day3.txt")
file.each {|line|
  sides = line.scan(/\d+/)
  sides = sides.collect { |x| x.to_i }
  triangle = Triangle.new(sides)
  if triangle.is_possible?
    possible += 1
  else
    impossible += 1
  end
}

puts "Total number of triangles: "
puts possible + impossible
puts "Number of possible triangles: "
puts possible
puts "Number of impossible triangles: "
puts impossible