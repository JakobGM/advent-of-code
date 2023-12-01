use std::error::Error;
use std::fs;

fn find_first(line: &str) -> Option<char> {
    for char in line.chars() {
        if char.is_digit(10) {
            return Some(char);
        }
    }
    None
}

fn find_last(line: &str) -> Option<char> {
    for char in line.chars().rev() {
        if char.is_digit(10) {
            return Some(char);
        }
    }
    None
}

fn part1(problem: &str) -> Option<usize> {
    let mut sum: usize = 0;
    for line in problem.trim().split("\n") {
        let first = find_first(line)?;
        let second = find_last(line)?;
        let number: usize = format!("{first}{second}").parse().unwrap();
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
