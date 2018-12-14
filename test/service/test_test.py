import pytest
from service.exception import ServiceException
from service.test import ServiceTest

class TestClass(object):
  def sampleData(self):
    return {'records': [1, 2, 3, 4]}

  def goodService(self):
    return ServiceTest({'success': True, 'data': self.sampleData()})

  def test_goodService(self):
    assert self.goodService().get('/test.json') == self.sampleData()

  def test_noSuccess(self):
    with pytest.raises(ServiceException, message = ''):
        ServiceTest({}).get('/test.json')

  def test_unsuccessfuly(self):
    with pytest.raises(ServiceException, message = ''):
      ServiceTest({'success': False}).get('/test.json')

  def test_unsuccessfulyWithMessage(self):
    with pytest.raises(ServiceException, message = 'Exceptional message'):
      ServiceTest({'success': False, 'message': 'Exceptional message'}).get('/test.json')