// Digit factorials
// Problem 34
// 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
//
// Find the sum of all numbers which are equal to the sum of the factorial of their digits.
//
// Note: as 1! = 1 and 2! = 2 are not sums they are not included.

object Euler034 extends App {
  // compute factorials up front
  def factorial(n: Int): Int = (1 to n).foldLeft(1)(_ * _)
  val factorials = (0 to 9).toArray.map(factorial)

  // function to check if number is sum of factorials of digits
  def isFactorialSum(n: Int): Boolean = n == n.toString().toCharArray().foldLeft(0){(acc, x) => acc + factorials(x.toInt - 48)}

  // compute the answer
  val answer = (3 to 2540161).filter(isFactorialSum).sum
  println(answer)
}
