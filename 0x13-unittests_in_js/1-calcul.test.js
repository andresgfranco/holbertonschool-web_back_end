const { calculateNumber } = require('./1-calcul');

const assert = require("assert");

describe("integer cases", function() {
  it("integer case1", function() {
    assert.equal(calculateNumber('SUM', 2, 3), 5);
  });
  it("integer case2", function() {
    assert.equal(calculateNumber('SUBTRACT', 0, 2), -2);
  });
  it("integer case3", function() {
    assert.equal(calculateNumber('DIVIDE', 2, 2), 1);
  });
  it("integer case4", function() {
    assert.equal(calculateNumber('DIVIDE', 0, 0), 'Error');
  });
});

describe("float cases", function() {
  it("float case1", function() {
    assert.equal(calculateNumber('SUM', 0.00000001, 2), 2);
  });
  it("float case2", function() {
    assert.equal(calculateNumber('SUBTRACT', 0.99, 2), -1);
  });
  it("float case3", function() {
    assert.equal(calculateNumber('DIVIDE', 0.99999999, 2), 0.5);
  });
  it("float case4", function() {
    assert.equal(calculateNumber('DIVIDE', 0.51, 0.40), 'Error');
  });
  });

describe("undefined case", function() {
  it("undefined case5", function() {
    assert.equal(calculateNumber('SOMEeeee', 0.51, 5.49), undefined);
  });
});
