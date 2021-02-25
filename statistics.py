import numpy as np

CAR_STREET_DISCOUNT_FACTOR = 1

def street_usage(cars, streets):
    for car in cars:
        for i, street in enumerate(car.streets):
            streets[street.name].number_of_cars_uses_it += (
                CAR_STREET_DISCOUNT_FACTOR**i)

def intersection_loader(intersections, streets):
    for street in streets.values():
        intersections[street.end].in_streets.append(street)
        intersections[street.begin].out_streets.append(street)

def filter_streets(intersection):
    intersection.in_streets = list(
        filter(lambda s: s.number_of_cars_uses_it != 0,
               intersection.in_streets))

def ratio_of_streets(intersections):
    for intersection in intersections:
        summ = 0
        for street in intersection.in_streets:
            summ += street.number_of_cars_uses_it

        if summ == 0:
            for street in intersection.in_streets:
                intersection.in_street_ratios.append(0)
        else:
            filter_streets(intersection)
            for street in intersection.in_streets:
                intersection.in_street_ratios.append(
                    street.number_of_cars_uses_it / summ)

def route_length_stats(world):
    lengths = np.array(
        [sum(s.length for s in car.streets) for car in world.cars])
    return {
        'min_route_len': float(lengths.min()),
        'max_route_len': float(lengths.max()),
        'avg_route_len': float(lengths.mean()),
        'std_route_len': float(lengths.std()),
        'median_route_len': float(np.median(lengths)),
        '10th_pct_route_len': float(np.quantile(lengths, 0.1)),
        '90th_pct_route_len': float(np.quantile(lengths, 0.9)),
    }

def ratio_distributions_of_intersections(intersections):
    for intersection in intersections:
        print(np.std(intersection.in_street_ratios))
