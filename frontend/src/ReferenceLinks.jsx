import React from 'react';

function ReferenceLinks({ links }) {
  return (
    <ul>
      {links.map((link, index) => (
        <li key={index}>
          <a href={link} target="_blank" rel="noopener noreferrer">{link}</a>
        </li>
      ))}
    </ul>
  );
}

export default ReferenceLinks;
