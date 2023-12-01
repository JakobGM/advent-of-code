use std::error::Error;
use std::fs;

fn part1(problem: &str) -> Option<usize> {
    let mut sum: usize = 0;
    for line in problem.trim().lines() {
        let first_digit = line.chars().filter(|c| c.is_digit(10)).next().unwrap();
        let last_digit = line.chars().rev().filter(|c| c.is_digit(10)).next()?;
        let number: usize = format!("{first_digit}{last_digit}").parse().unwrap();
        sum += number;
    }
    Some(sum)
}

fn main() -> Result<(), Box<dyn Error>> {
    let problem = fs::read_to_string("input/1.txt")?;
    let solution = part1(&problem).unwrap();
    println!("Part 1: {solution}");
    Ok(())
}
