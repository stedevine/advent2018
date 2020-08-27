from collections import namedtuple
def main():
    Point = namedtuple('Point', ['x','y','vx','vy'])
    points = []
    with open('./10-1-input.txt') as input_file:
        lines = input_file.readlines()
        for line in lines:
            x = int(line.split('<')[1].split(',')[0])
            y = int(line.split(',')[1].split('>')[0])
            vx = int(line.split('<')[2].split(',')[0])
            vy = int(line.split(',')[2].split('>')[0])
            points.append(Point(x=x, y=y, vx=vx, vy=vy))

    print('parsed')
    seconds = 0
    while print_points(points):
        points = advance_points(points)
        seconds = seconds + 1
    print('time taken {}'.format(seconds))

def advance_points(points):
    new_points = []
    for p in points:
        p = p._replace(x=p.x + p.vx)
        p = p._replace(y=p.y + p.vy)
        new_points.append(p)
    return new_points


def print_points(points):
    min_x = min(p.x for p in points)
    max_x = max(p.x for p in points)
    min_y = min(p.y for p in points)
    max_y = max(p.y for p in points)

    if(max_y - min_y < 10):
        print('x {} {}'.format(min_x,max_x))

        print('y {} {}'.format(min_y,max_y))


        for y in range (min_y, max_y+1):
            line = ''
            for x in range (min_x, max_x+1):
                # print('{}{}'.format(y,x))
                if (x,y) in [(p.x,p.y) for p in points]:
                    line = line + '#'
                else:
                    line = line + '.'
            print(line)
        return False
    else:
        return True

if __name__ == '__main__':
    main()
