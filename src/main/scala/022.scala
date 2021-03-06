// Names scores
// Problem 22
// Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
//
// For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
//
// What is the total of all the name scores in the file?

import scala.io.Source

object Euler022 extends App {
  val names = Source.fromFile("../../resources/022.txt").mkString.split(',').map(_.replace(""""""", "")).sorted

  val scores = names.zipWithIndex.foldLeft(0) {(s,n) => nameValue(n._1) * (n._2 + 1) + s}

  println(scores)

  def nameValue(name: String): Int = name.toCharArray.map(_.toInt - 64).sum
}
