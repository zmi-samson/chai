
import unittest
from collections import deque

from chai import Chai
from chai.exception import *

class CupOf(Chai):
  def test_something(self): pass
  def runTest(self, *args, **kwargs): pass

class ChaiTest(unittest.TestCase):

  def test_init(self):
    case = CupOf.__new__(CupOf)
    self.assertTrue( hasattr(case, 'assertEquals') )
    self.assertFalse( hasattr(case, 'assert_equals') )
    case.__init__()
    self.assertTrue( hasattr(case, 'assertEquals') )
    self.assertTrue( hasattr(case, 'assert_equals') )

  def test_setup(self):
    case = CupOf()
    case.setup()
    self.assertEquals( deque(), case._stubs )
    self.assertEquals( deque(), case._mocks )

  def test_teardown_closes_out_stubs_and_mocks(self):
    class Stub(object):
      calls = 0
      def assert_expectations(self): self.calls += 1
      def teardown(self): self.calls += 1

    obj = type('test',(object,),{})()
    setattr(obj, 'mock1', 'foo')
    setattr(obj, 'mock2', 'bar')
    
    case = CupOf()
    stub = Stub()
    case._stubs = deque([stub])
    case._mocks = deque([(obj,'mock1','fee'), (obj,'mock2')])
    case.teardown()
    self.assertEquals( 2, stub.calls )
    self.assertEquals( 'fee', obj.mock1 )
    self.assertFalse( hasattr(obj, 'mock2') )

  def test_teardown_closes_out_stubs_and_mocks_when_exception(self):
    class Stub(object):
      calls = 0
      def assert_expectations(self): self.calls += 1; raise ExpectationNotSatisfied('blargh')
      def teardown(self): self.calls += 1

    obj = type('test',(object,),{})()
    setattr(obj, 'mock1', 'foo')
    setattr(obj, 'mock2', 'bar')
    
    case = CupOf()
    stub = Stub()
    case._stubs = deque([stub])
    case._mocks = deque([(obj,'mock1','fee'), (obj,'mock2')])
    self.assertRaises( ExpectationNotSatisfied, case.teardown )
    self.assertEquals( 2, stub.calls )
    self.assertEquals( 'fee', obj.mock1 )
    self.assertFalse( hasattr(obj, 'mock2') )
