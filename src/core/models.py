from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, JSON
from sqlalchemy.orm import relationship

from db.session import Base


class Tags(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    # attractions = relationship("Attractions", back_populates="attractions_tags")
    # restaurants = relationship("Restaurants", back_populates="restaurants_tags")


class Content(Base):
    __tablename__ = 'content'
    id = Column(Integer, primary_key=True)
    content_type = Column(String, nullable=False)
    content_id = Column(Integer, nullable=False)
    data = Column(String, nullable=False)
    image_urls = Column(JSON, nullable=True)

    attraction = relationship(
        "Attractions",
        back_populates="content",
        primaryjoin="and_(Attractions.id == foreign(Content.content_id), Content.content_type=='attractions')"
    )

    hotel = relationship(
        "Hotels",
        back_populates="content",
        primaryjoin="and_(Hotels.id == foreign(Content.content_id), Content.content_type=='hotels')"
    )

    restaurant = relationship(
        "Restaurants",
        back_populates="content",
        primaryjoin="and_(Restaurants.id == foreign(Content.content_id), Content.content_type=='restaurants')"
    )

    user_travel_experience = relationship(
        "UserTravelExperiences",
        back_populates="content",
        primaryjoin="and_(UserTravelExperiences.id == foreign(Content.content_id), Content.content_type=='user_travel_experiences')",
    )

    review = relationship(
        "Reviews",
        back_populates="content",
        primaryjoin="and_(Reviews.id == foreign(Content.content_id), Content.content_type=='reviews')"
    )

    # user = relationship(
    #     "User",
    #     back_populates="content",
    #     primaryjoin="and_(User.id == foreign(Content.content_id), Content.content_type=='users')"
    # )


class RestaurantsTags(Base):
    __tablename__ = 'restaurants_tags'
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.id'), primary_key=True)


class AttractionsTags(Base):
    __tablename__ = 'attractions_tags'
    attraction_id = Column(Integer, ForeignKey('attractions.id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.id'), primary_key=True)
