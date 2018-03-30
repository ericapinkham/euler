// Maximum path sum II
// Problem 67
// By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
//
// 3
// 7 4
// 2 4 6
// 8 5 9 3
//
// That is, 3 + 7 + 4 + 9 = 23.
//
// Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
//
// // NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
import scala.annotation.tailrec
import scala.io.Source

object Euler067 extends App {
  // read the file
  val lines = Source.fromFile("../../resources/067.txt").getLines().map(_.split(' ').map(_.toInt).toList).toList

  // Execute
  println(processTriangle(lines.reverse))

  // main processing method
  def processTriangle(triangle: List[List[Int]]): Int = triangle match {
    case r1 :: r2 :: rs => processTriangle(((pairwiseMax(r1) zip r2).map{case (x,y) => x + y}) :: rs)
    case r1 :: _ => r1.head
  }

  //
  def pairwiseMax(row: List[Int]): List[Int] = {
    @tailrec
    def acc(maxes: List[Int], unprocessed: List[Int]): List[Int] = unprocessed match {
      case x1 :: Nil => maxes
      case x1 :: x2 :: xs => acc((x1 max x2) :: maxes, x2 :: xs)
      case Nil => throw new Error(s"Unexpected case")
    }

    acc(List[Int](), row).reverse
  }
}
