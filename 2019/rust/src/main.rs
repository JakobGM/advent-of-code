use std::fs::read_to_string;

use aoc::days::{DayOne, DayX};
use aoc::problem::Solver;
use clap::Parser;

#[derive(Parser, Debug)]
struct Args {
    day: usize,
}

fn day_to_solver(day: usize) -> Box<dyn Solver> {
    match day {
        1 => Box::new(DayOne {}),
        _ => Box::new(DayX {}),
    }
}

fn main() {
    let args = Args::parse();
    let solver = day_to_solver(args.day);
    let input = read_to_string(format!("input/{}.txt", args.day)).expect(&format!(
        "Problem input not downloaded for day {}!",
        args.day
    ));
    println!("Part one: {}", solver.part_one(&input));
    println!("Part two: {}", solver.part_two(&input));
}
