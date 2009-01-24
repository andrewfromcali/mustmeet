class FacebookController < ApplicationController
  before_filter :require_facebook_login
  
  def index
    response = fbsession.users_getInfo(:uids => fbsession.friends_get.uid_list, 
                                       :fields => [:name, :pic_small])
    @list = response.user_list
  end
  
  def test
  end
  
end
