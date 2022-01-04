const { calculateNumber } = require('./0-calcul');

const assert = require("assert");

describe("integer cases", function() {
  it("integer case1", function() {
    assert.equal(calculateNumber(2, 3), 5);
  });
  it("integer case2", function() {
    assert.equal(calculateNumber(0, 2), 2);
  });
  it("integer case3", function() {
    assert.equal(calculateNumber(2, 2), 4);
  });
  it("integer case4", function() {
    assert.equal(calculateNumber(0, 0), 0);
  });

  it("float case1", function() {
    assert.equal(calculateNumber(0.00000001, 2), 2);
  });
  it("float case2", function() {
    assert.equal(calculateNumber(0.99, 2), 3);
  });
  it("float case3", function() {
    assert.equal(calculateNumber(0.99999999, 2), 3);
  });
  it("float case4", function() {
    assert.equal(calculateNumber(0.51, 5.50), 7);
  });
  it("float case5", function() {
    assert.equal(calculateNumber(0.51, 5.49), 6);
  });
});
