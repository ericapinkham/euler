// Permuted multiples
// Problem 52
// It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
//
// Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

object Euler052 extends App {

  println(Stream.from(1).filter(allSameDigits).head)

  def allSameDigits(x: Int): Boolean = sameDigits(x, 2 * x) && sameDigits(x, 3 * x) && sameDigits(x, 4 * x) && sameDigits(x, 5 * x) && sameDigits(x, 6 * x)

  def sameDigits(x: Int, y: Int): Boolean = x.toString.toCharArray.toSet == y.toString.toCharArray.toSet
}
