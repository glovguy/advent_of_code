class Triangle
  attr_accessor :sides
  protected :sides

  def initialize(sides)
    sides = Array.new(sides) unless sides.is_a? Array
    @sides = sides.sort
  end

  def is_possible?
      if @sides[2] < @sides[0] + @sides[1]
        return true
      else
        return false
      end
  end
end