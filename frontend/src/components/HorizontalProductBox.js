import React from 'react';
// import './Featured.css';

function Featured() {
  const items = [
    {
      id: 1,
      image: 'https://picsum.photos/200/300',
      title: 'Item 1',
      description: 'Lorem ipsum .',
    },
    {
      id: 2,
      image: 'https://picsum.photos/200/300',
      title: 'Item 2',
      description: 'Lorem ipsum .',
    },
    {
      id: 3,
      image: 'https://picsum.photos/200/300',
      title: 'Item 3',
      description: 'Lorem ipsum .',
    },
    {
      id: 4,
      image: 'https://picsum.photos/200/300',
      title: 'Item 4',
      description: 'Lorem ipsum .',
    },
    {
      id: 5,
      image: '',
      title: 'Item 5',
      description: 'Lorem ipsum .',
    },
    {
      id: 6,
      image: 'https://picsum.photos/200/300',
      title: 'Item 6',
      description: 'Lorem ipsum .',
    },
  ];

  return (
    <div className="featured-container">
      <h1 className="featured-title">Featured Items</h1>
      <div className="featured-scroll">
        {items.map((item) => (
          <div className="featured-item" key={item.id}>
            <img className="featured-image" src={item.image} alt={item.title} />
            <h2 className="featured-item-title">{item.title}</h2>
            <p className="featured-item-description">{item.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Featured;
