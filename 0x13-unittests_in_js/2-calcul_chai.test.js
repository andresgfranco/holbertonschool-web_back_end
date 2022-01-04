const { calculateNumber } = require('./1-calcul');
const expect = require('chai').expect


describe("integer cases", function () {
  it("integer case1", function () {
    expect(calculateNumber('SUM', 2, 3)).to.equal(5);
  });
  it("integer case2", function () {
    expect(calculateNumber('SUBTRACT', 0, 2)).to.equal(-2);
  });
  it("integer case3", function () {
    expect(calculateNumber('DIVIDE', 2, 2)).to.equal(1);
  });
  it("integer case4", function () {
    expect(calculateNumber('DIVIDE', 0, 0)).to.equal('Error');
  });
});

describe("float cases", function () {
  it("float case1", function () {
    expect(calculateNumber('SUM', 0.00000001, 2)).to.equal(2);
  });
  it("float case2", function () {
    expect(calculateNumber('SUBTRACT', 0.99, 2)).to.equal(-1);
  });
  it("float case3", function () {
    expect(calculateNumber('DIVIDE', 0.99999999, 2)).to.equal(0.5);
  });
  it("float case4", function () {
    expect(calculateNumber('DIVIDE', 0.51, 0.40)).to.equal('Error');
  });
});

describe("undefined case", function () {
  it("undefined case5", function () {
    expect(calculateNumber('SOMEeeee', 0.51, 5.49)).to.equal(undefined);
  });
});

