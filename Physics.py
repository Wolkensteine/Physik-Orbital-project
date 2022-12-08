import math
import plotly.express as px

gravitational_constant = 6.67259 * (10 ** -11)
earth_radius = 6.37104 * (10 ** 6)
earth_mass = 5.9736 * (10 ** 24)

range_begin = 6.6184
range_end = 6.6186

increase = 0.00001

give_start_orbit_height_above_earth = 400000
given_specific_impulse = 4000
given_mass_ratio = 10

minimum_difference_needed_provided_delta_velocity_transfer_finale_orbit = 1000000
minimum_difference_needed_provided_delta_velocity_transfer_finale_orbit_position = 0


def total_delta_velocity(specific_impulse, mass_ratio):
    return specific_impulse * math.log(mass_ratio)


def circular_orbit_velocity(central_mass, radius):
    return math.sqrt((gravitational_constant * central_mass) / radius)


def get_elliptical_orbit_apoapsis_velocity(central_mass, height_periapsis, height_apoapsis):
    return math.sqrt((2 * gravitational_constant * central_mass) / (height_periapsis + height_apoapsis) *
                     height_periapsis / height_apoapsis)


def get_elliptical_orbit_apoapsis_height(central_mass, height_periapsis, velocity_periapsis):
    return (2 * gravitational_constant * central_mass) / (velocity_periapsis ** 2) + height_periapsis


if __name__ == "__main__":
    print("Starting simulation ...")
    i = range_begin
    while i < range_end:
        start_radius = give_start_orbit_height_above_earth + earth_radius
        print("r0 = " + str(start_radius))

        start_velocity = circular_orbit_velocity(earth_mass, start_radius)
        print("V0 = " + str(start_velocity))
        print()

        dv1 = round(100 - i, 5)
        dv2 = round(i, 5)
        print("dV1 : dV2 => " + str(dv1) + " : " + str(dv2))

        delta_velocity = total_delta_velocity(given_specific_impulse, given_mass_ratio)
        print("dV = " + str(delta_velocity))

        delta_velocity_one = delta_velocity / 100 * dv1
        print("dV1 = " + str(delta_velocity_one))

        delta_velocity_two = delta_velocity / 100 * dv2
        print("dV2 = " + str(delta_velocity_two))
        print()

        periapsis_velocity_transfer_orbit = start_velocity + delta_velocity_one
        print("Transfer orbit periapsis v = " + str(periapsis_velocity_transfer_orbit))

        periapsis_height_transfer_orbit = start_radius
        print("Transfer orbit periapsis r = " + str(periapsis_height_transfer_orbit))

        apoapsis_height_transfer_orbit = get_elliptical_orbit_apoapsis_height(earth_mass, start_radius,
                                                                              periapsis_velocity_transfer_orbit)
        print("Transfer orbit apoapsis r = " + str(apoapsis_height_transfer_orbit))

        apoapsis_velocity_transfer_orbit = get_elliptical_orbit_apoapsis_velocity(earth_mass,
                                                                                  periapsis_height_transfer_orbit,
                                                                                  apoapsis_height_transfer_orbit)
        print("Transfer orbit apoapsis v = " + str(apoapsis_velocity_transfer_orbit))
        print()

        required_velocity_final_orbit = circular_orbit_velocity(earth_mass, apoapsis_height_transfer_orbit)
        print("Required speed for final circular orbit v = " + str(required_velocity_final_orbit))

        delta_velocity_transfer_final_orbit = required_velocity_final_orbit - apoapsis_velocity_transfer_orbit
        print("Required velocity change from transfer to final orbit dV = " + str(delta_velocity_transfer_final_orbit))
        print()

        print("cur best dv1: " + str(minimum_difference_needed_provided_delta_velocity_transfer_finale_orbit_position))
        print("cur best dv2: " + str(minimum_difference_needed_provided_delta_velocity_transfer_finale_orbit))
        print("this dv1: " + str(dv1))
        print("this dv2: " + str(delta_velocity_two - delta_velocity_transfer_final_orbit))
        print()
        if minimum_difference_needed_provided_delta_velocity_transfer_finale_orbit > \
                (delta_velocity_two - delta_velocity_transfer_final_orbit) > \
                -1 * minimum_difference_needed_provided_delta_velocity_transfer_finale_orbit:
            print("This dv2 is better then the current best. Changing this ...")
            minimum_difference_needed_provided_delta_velocity_transfer_finale_orbit = \
                delta_velocity_two - delta_velocity_transfer_final_orbit
            minimum_difference_needed_provided_delta_velocity_transfer_finale_orbit_position = dv1

        i += increase
        i = round(i, 5)

    print("Simulation done.")
    print("Best dV2 delta: " + str(minimum_difference_needed_provided_delta_velocity_transfer_finale_orbit))
    print("Best dV1: " + str(minimum_difference_needed_provided_delta_velocity_transfer_finale_orbit_position))
