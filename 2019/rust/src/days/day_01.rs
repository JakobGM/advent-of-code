use crate::problem::Solver;

pub struct DayOne;

impl DayOne {
    fn parse(&self, input: &str) -> Vec<i32> {
        input
            .trim()
            .split('\n')
            .map(|s| s.parse::<i32>().unwrap())
            .collect()
    }
}

impl Solver for DayOne {
    fn part_one(&self, input: &str) -> String {
        let numbers = self.parse(input);
        let part_1: i32 = numbers.iter().map(|m| required_fuel(&m)).sum();
        part_1.to_string()
    }

    fn part_two(&self, input: &str) -> String {
        let numbers = self.parse(input);
        let part_2: i32 = numbers.iter().map(|m| total_required_fuel(&m)).sum();
        part_2.to_string()
    }
}

fn required_fuel(mass: &i32) -> i32 {
    mass / 3 - 2
}

fn total_required_fuel(mass: &i32) -> i32 {
    let mut total = 0;
    let mut new_fuel = required_fuel(mass);
    while new_fuel > 0 {
        total += new_fuel;
        new_fuel = required_fuel(&new_fuel);
    }
    total
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn required_fuel_works() {
        assert_eq!(required_fuel(&12), 2);
        assert_eq!(required_fuel(&14), 2);
        assert_eq!(required_fuel(&1969), 654);
        assert_eq!(required_fuel(&100756), 33583);
    }

    #[test]
    fn total_required_fuel_works() {
        assert_eq!(total_required_fuel(&14), 2);
        assert_eq!(total_required_fuel(&1_969), 966);
        assert_eq!(total_required_fuel(&100_756), 50_346);
    }
}
