require 'rspec'
require_relative 'day3'

RSpec.describe Triangle do
  # subject(:possible_triangle) { Triangle.new(1,3,3) }
  # subject(:impossible_triangle) { Triangle.new(1,2,3) }

  it "knows when it is a possible triangle" do
    expect(Triangle.new([2,3,4]).is_possible?).to eq(true)
    expect(Triangle.new([1,2,3]).is_possible?).to eq(false)
    # expect(teaspoon == Object.new).to eq(false)
    # expect(teaspoon == nil).to eq(false)
  end

end


# """class test_day3(unittest.TestCase):
#     def test_is_valid_triangle(self):
#         self.assertEqual(is_valid_triangle([2,3,4]), True)
#         self.assertEqual(is_valid_triangle([4,3,2]), True)
#         self.assertEqual(is_valid_triangle([3,2,4]), True)
#         self.assertEqual(is_valid_triangle([1,2,4]), False)
#         self.assertEqual(is_valid_triangle([1,2,10]), False)
#         self.assertEqual(is_valid_triangle([1,2,3]), False)"""