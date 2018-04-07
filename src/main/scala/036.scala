// Double-base palindromes
// Problem 36
// The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
//
// Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
//
// (Please note that the palindromic number, in either base, may not include leading zeros.)
import scala.annotation.tailrec

object Euler036 extends App {
  println((1 to 1000000).filter(isDualPalindrome).sum)

  // determine if a string is a palindrome
  def isPalindrome(ca: String): Boolean = {
    val half = ca.length / 2
    ca.slice(0, half) == ca.reverse.slice(0, half)
  }

  def isDualPalindrome(n: Int): Boolean = isPalindrome(n.toString) && isPalindrome(n.toBinaryString)
}
