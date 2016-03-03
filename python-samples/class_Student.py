class Student(object):

      #def __init__(self,name,score):
      #     self.__name =name
      #      self.__score=score

      def print_score(self):
            print('%s :%s' %(self.__name,self.__score))

      def get_name(self):
            return self.__name

      def get_score(self):
            return self._score

      def set_score(self,value):
            if not isinstance(value,int):
                  raise ValueError('score must be an integer!')
            if value<0 or value>100:
                  raise ValueError('score must between 0~100!')
            self._score=value

      @property
      def score(self):
            return self._score

      @score.setter
      def score(self,value):
            if not isinstance(value,int):
                  raise ValueError('score must be an integer!')
            if value<0 or value>100:
                  raise ValueError('score must between 0~100！')
            self._score=value

      @property
      def birth(self):
            return self._birth

      @birth.setter
      def birth(self,value):
            self._birth=value

      @property
      def age(self):
            return 2016 - self._birth
