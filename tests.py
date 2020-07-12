''' File to run automated unit tests. Will keep adding as we create more features '''

import unittest
from app import app, db
from app.models import User, Turnstile, TurnstileGroup

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='test')
        u.set_password('correct')
        self.assertFalse(u.check_password('incorrect'))
        self.assertTrue(u.check_password('correct'))

    # test getting a followed turnstile from the turnstile group
    def test_getting_turnstile_from_group(self):
        g1 = TurnstileGroup(group_id='gx1', location='SE')
        db.session.add(g1)
        db.session.commit()

        t1 = Turnstile(turnstile_id='tx1', group_id='gx1')
        t2 = Turnstile(turnstile_id='tx2', group_id='gx1')
        t3 = Turnstile(turnstile_id='tx3', group_id='gx2')
        db.session.add_all([t1, t2, t3])
        db.session.commit()
        
        # let's check the turnstiles match
        group1 = g1.turnstiles.all()
        self.assertEqual(group1, [t1, t2])

        empty_group = t3.group
        self.assertIsNone(empty_group)

    # test seeing if the total_count of a turnstile group is equal to total of its turnstiles
    # test if the total_rate of a turnstile group corresponds to what it should be corresponding to the individuals
    # test updating the database we're retrieving from and retrieving


# run the test battery
if __name__ == '__main__':
    unittest.main(verbosity=2)
