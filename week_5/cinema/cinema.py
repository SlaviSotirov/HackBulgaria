from connection import Base
from movie import Movie
from projection import Projection
from reservation import Reservation
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import func


class Cinema:

    def __init__(self, engine):
        self.engine = engine
        self.session = Session(bind=engine)

    def add_movie(self, movie):
        self.session.add(movie)
        self.session.commit()

    def show_movies(self):
        for movie in self.session.query(Movie).order_by(Movie.rating.desc()).all():
            print(movie)

    def add_projection(self, projection):
        self.session.add(projection)
        self.session.commit()

    #add date option
    def show_movie_projections(self, id):
        for proj in self.session.query(Projection).filter(Projection.movie_id == id).all():
############DO NOT PRINT
            print(proj)

    def seats_for_projection(self, projection_id):
        seats = self.session.query(Reservation).filter(Reservation.projection_id == projection_id).count()
        return 100 - int(seats)

    def print_seats(self, seats):
        result = ''
        for row in seats:
            for seat in row:
                result += seat + " "
            result += "\n"

        return result

    def show_availabe_seats(self, projection_id):
        seats = [["." for i in range(10)] for k in range(10)]
        for reservation in self.session.query(Reservation).filter(Reservation.projection_id == projection_id):
            seats[reservation.col][reservation.row] = "x"
        return self.print_seats(seats)

    def _is_seat_availabe(self, hall_seats, seat):
        if seat[0] > 10 or seat[1] > 10:
            return False
        for hall_seat in hall_seats:
            if hall_seat == seat:
                return False
        return True

    def _enter_seat_position(self):
        position = input("Insert seat position: ")
        #magic
        position = tuple([int(x)-1 for x in position.strip("()").split(",")])
        return position

    def reserve_seats(self, tickets_count, projection_id, uname):
        seats = self._get_seats_in_list(projection_id)

        for i in range(tickets_count):
            seat = self._enter_seat_position()
            while not self._is_seat_availabe(seats, seat):
                print("Invalid seat position")
                seat = self._enter_seat_position()
            reservation = self.make_reservation(uname, seat[0], seat[1], projection_id)
            self.session.add(reservation)

    def _get_seats_in_list(self, projection_id):
        seats = []
        for reservation in self.session.query(Reservation).filter(Reservation.projection_id == projection_id):
            seats.append((reservation.row-1, reservation.col-1))
        return seats

    def make_reservation(self, username, col, row, projection_id):
        return Reservation(username=username, col=col, row=row, projection_id=projection_id)

    def finalize_reservations(self):
        self.session.commit()

    def cancel_reservation(self):
        pass
    ########revert session commit


def main():
    engine = create_engine("sqlite:///cinema.db")
    Base.metadata.create_all(engine)
    cinema = Cinema(engine)
    # riddick = Movie(name="Riddick", rating="10")
    # cinema.add_movie(riddick)
    # riddick2 = Movie(name="Riddick2", rating="10")
    # cinema.add_movie(riddick2)
    # slab_film = Movie(name="Twilight", rating=2)
    # qk_film = Movie(name="NeZdrach", rating=7)
    # cinema.add_movie(slab_film)
    # cinema.add_movie(qk_film)
    # riddick_3d = Projection(type="3D", date="Today", time="Later", movie_id=1)
    # riddick2_3d = Projection(type="3D", date="Today", time="Later", movie_id=2)
    # cinema.add_projection(riddick_3d)
    # cinema.add_projection(riddick2_3d)
    # cinema.show_movies()
    # print(cinema.seats_for_projection(1))
    # cinema.show_availabe_seats(1)
    # cinema.show_movie_projections(1)
    cinema.reserve_seats(1, 1, "Slavi")
    print(cinema.show_availabe_seats(1))
    # cinema.reserve_seats(2, 1)


if __name__ == '__main__':
    main()
