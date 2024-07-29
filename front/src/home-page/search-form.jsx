import React, { useState, useEffect } from 'react';
import "./search-form.scss";

const Search = () => {
    const [showPanel, setShowPanel] = useState(false);
    const [searchTerm, setSearchTerm] = useState('');
    const [searchJson, setSearchJson] = useState([]);

    const fetchSearchResults = (term) => {
        fetch(`http://localhost:5000/search?query=${term}`)
            .then(response => response.json())
            .then(data => {
                console.log('Fetched data:', data);
                if (Array.isArray(data)) {
                    setSearchJson(data);
                } else {
                    console.error('Unexpected data format:', data);
                    setSearchJson([]);
                }
            })
            .catch(error => {
                console.error('Error fetching search results', error);
            });
    };

    // Effect to perform search when searchTerm changes
    useEffect(() => {
        if (searchTerm) {
            fetchSearchResults(searchTerm);
        } else {
            setSearchJson([]); // Clear results if searchTerm is empty
        }
    }, [searchTerm]);

    const onInput = (event) => {
        setShowPanel(!showPanel);

        if (event.nativeEvent.inputType === 'insertText') {
            setSearchTerm(prevTerm => prevTerm + event.target.value.slice(-1));
        } else {
            setSearchTerm(prevTerm => prevTerm.slice(0, -1));
        }
    };

    return (
        <div className='search'>
            <input type="text" value={searchTerm} onInput={onInput} placeholder="Search term"  />
            {showPanel && (
                <div className="panel">
                    {searchJson.map(item => (
                        <div key={item.flight_number} className='panelChild'>
                            <p>{item.flight_number}</p>
                            <p>{item.status}</p></div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default Search;
