require 'rspec'
require_relative 'day3'

RSpec.describe Triangle do

  it "knows when it is a possible triangle" do
    expect(Triangle.new([2,3,4]).is_possible?).to eq(true)
    expect(Triangle.new([1,2,3]).is_possible?).to eq(false)
    expect(Triangle.new([4,3,2]).is_possible?).to eq(true)
    expect(Triangle.new([3,2,4]).is_possible?).to eq(true)
    expect(Triangle.new([1,2,4]).is_possible?).to eq(false)
    expect(Triangle.new([1,2,10]).is_possible?).to eq(false)
    expect(Triangle.new([1,2,3]).is_possible?).to eq(false)
  end

end
