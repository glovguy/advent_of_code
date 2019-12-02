function fuel_for_module(mod) {
  return Math.floor(mod / 3.0) - 2;
}

function result_one() {
  return input.split('\n').map(fuel_for_module).reduce((acc, fuel) => acc + fuel);
}

function fuel_for_module_part_two(mod) {
  let tot = 0;
  let fuelNeeded = mod;
  while (fuelNeeded > 0) {
    const fuel = fuel_for_module(fuelNeeded);
    if (fuel <= 0) { break; }
    fuelNeeded = fuel;
    tot += fuel;
  }
  return tot;
}

function result_two() {
  return input.split('\n').map(fuel_for_module_part_two).reduce((acc, fuel) => acc + fuel);
}

const input = `74099
50130
81867
55356
73088
73706
55902
113399
129578
78051
117663
137454
66285
115389
50547
51588
115792
91085
118882
109486
135616
107771
90105
101182
54766
86615
91261
104321
121607
82197
68626
111255
136080
87509
70125
91180
75925
53492
96853
115081
121621
87461
116030
67335
61282
112424
106785
142243
110564
56983
131420
116534
117376
147088
117628
53964
73163
106736
76217
128590
116138
66841
109265
106285
64013
78357
125640
145761
139426
127558
135076
130989
68054
134669
144482
125870
112818
60193
107162
112557
115972
50890
148652
89547
120228
85967
103941
130915
129496
66401
87018
149539
105847
60981
82610
134396
121711
142655
104400
103752`;

console.log('Part one: ', result_one());
console.log('Part two: ', result_two());
