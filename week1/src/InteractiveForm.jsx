import React, { useState } from 'react';

function InteractiveForm() {
  const [formData, setFormData] = useState({
    name: '',
    favoriteColor: '',
    hobbies: [],
    gender: '',
    country: '',
    newsletter: false,
    experience: ''
  });

  const handleInputChange = (e) => {
    const { name, value, type, checked } = e.target;
    
    if (type === 'checkbox' && name === 'hobbies') {
      setFormData(prev => ({
        ...prev,
        hobbies: checked 
          ? [...prev.hobbies, value]
          : prev.hobbies.filter(hobby => hobby !== value)
      }));
    } else if (type === 'checkbox') {
      setFormData(prev => ({
        ...prev,
        [name]: checked
      }));
    } else {
      setFormData(prev => ({
        ...prev,
        [name]: value
      }));
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Form submitted:', formData);
    alert('Form submitted! Check console for details.');
  };

  return (
    <div style={{ maxWidth: '600px', margin: '0 auto', padding: '20px' }}>
      <h2>Interactive Form</h2>
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
        
        {/* Text Input */}
        <div>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleInputChange}
            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
          />
        </div>

        {/* Dropdown */}
        <div>
          <label htmlFor="country">Country:</label>
          <select
            id="country"
            name="country"
            value={formData.country}
            onChange={handleInputChange}
            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
          >
            <option value="">Select a country</option>
            <option value="usa">United States</option>
            <option value="canada">Canada</option>
            <option value="uk">United Kingdom</option>
            <option value="germany">Germany</option>
            <option value="france">France</option>
            <option value="japan">Japan</option>
            <option value="australia">Australia</option>
          </select>
        </div>

        {/* Radio Buttons */}
        <div>
          <label>Gender:</label>
          <div style={{ marginTop: '5px' }}>
            <label style={{ display: 'block', marginBottom: '5px' }}>
              <input
                type="radio"
                name="gender"
                value="male"
                checked={formData.gender === 'male'}
                onChange={handleInputChange}
                style={{ marginRight: '8px' }}
              />
              Male
            </label>
            <label style={{ display: 'block', marginBottom: '5px' }}>
              <input
                type="radio"
                name="gender"
                value="female"
                checked={formData.gender === 'female'}
                onChange={handleInputChange}
                style={{ marginRight: '8px' }}
              />
              Female
            </label>
            <label style={{ display: 'block', marginBottom: '5px' }}>
              <input
                type="radio"
                name="gender"
                value="other"
                checked={formData.gender === 'other'}
                onChange={handleInputChange}
                style={{ marginRight: '8px' }}
              />
              Other
            </label>
          </div>
        </div>

        {/* Checkboxes */}
        <div>
          <label>Hobbies:</label>
          <div style={{ marginTop: '5px' }}>
            {['Reading', 'Gaming', 'Sports', 'Music', 'Cooking', 'Travel'].map(hobby => (
              <label key={hobby} style={{ display: 'block', marginBottom: '5px' }}>
                <input
                  type="checkbox"
                  name="hobbies"
                  value={hobby.toLowerCase()}
                  checked={formData.hobbies.includes(hobby.toLowerCase())}
                  onChange={handleInputChange}
                  style={{ marginRight: '8px' }}
                />
                {hobby}
              </label>
            ))}
          </div>
        </div>

        {/* Color Picker */}
        <div>
          <label htmlFor="favoriteColor">Favorite Color:</label>
          <input
            type="color"
            id="favoriteColor"
            name="favoriteColor"
            value={formData.favoriteColor}
            onChange={handleInputChange}
            style={{ width: '60px', height: '40px', marginTop: '5px', border: 'none' }}
          />
        </div>

        {/* Range Slider */}
        <div>
          <label htmlFor="experience">Experience Level: {formData.experience}</label>
          <input
            type="range"
            id="experience"
            name="experience"
            min="0"
            max="10"
            value={formData.experience}
            onChange={handleInputChange}
            style={{ width: '100%', marginTop: '5px' }}
          />
          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '12px', color: '#666' }}>
            <span>Beginner</span>
            <span>Expert</span>
          </div>
        </div>

        {/* Newsletter Checkbox */}
        <div>
          <label style={{ display: 'flex', alignItems: 'center' }}>
            <input
              type="checkbox"
              name="newsletter"
              checked={formData.newsletter}
              onChange={handleInputChange}
              style={{ marginRight: '8px' }}
            />
            Subscribe to newsletter
          </label>
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          style={{
            padding: '12px 24px',
            backgroundColor: '#007bff',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer',
            fontSize: '16px'
          }}
        >
          Submit Form
        </button>

        {/* Display Current Values */}
        <div style={{ 
          marginTop: '20px', 
          padding: '15px', 
          backgroundColor: '#f8f9fa', 
          borderRadius: '4px',
          fontSize: '14px'
        }}>
          <h3>Current Form Data:</h3>
          <pre>{JSON.stringify(formData, null, 2)}</pre>
        </div>
      </form>
    </div>
  );
}

export default InteractiveForm;