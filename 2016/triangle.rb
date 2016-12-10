class Triangle
  attr_accessor :sides
  protected :sides

  def initialize(sides)
    raise 'Incorrect number of sides' unless sides.length == 3
    @sides = sides.sort
  end

  def is_possible?
      if @sides[2] < @sides[0] + @sides[1]
        return true
      else
        return false
      end
  end

  def to_s
    @sides.join(",")
  end
end