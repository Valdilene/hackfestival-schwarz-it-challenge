import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {
  Grid,
  Card,
  CardContent,
  Typography,
  Container,
  Avatar,
  CardHeader,
  TextField,
  Button,
  Checkbox
} from '@mui/material';
import InventoryIcon from '@mui/icons-material/Inventory';

const ItemList = () => {
  const [items, setItems] = useState([]);
  const [today, setToday] = useState('');
  const [upcycleBuffer, setUpcycleBuffer] = useState(0);
  const [filterUpscale, setFilterUpscale] = useState(false);
  const [selectedItems, setSelectedItems] = useState([]);

  useEffect(() => {
    // Fetch data using axios
    axios.get('/api/articles')
      .then(response => {
        // Limit the data to the first 20 items
        const limitedData = response.data.slice(0, 20);
        setItems(response.data);
      })
      .catch(error => {
        console.error('Error fetching the data', error);
      });
  }, []);

  // Helper function to get the background color based on dates
  const getBackgroundColor = (expiresAt) => {
    const expiration = new Date(expiresAt);
    const todayDate = new Date(today);
    const bufferDate = new Date(todayDate);
    bufferDate.setDate(bufferDate.getDate() + upcycleBuffer);

    if (expiration < todayDate) {
      return '#F44336'; // Calm red background
    } else if (expiration < bufferDate) {
      return '#FFD54F'; // Warm yellow background
    }
    return 'white'; // Default background
  };

  // Filter items based on filterUpscale state
  const filteredItems = filterUpscale
    ? items.filter(item => getBackgroundColor(item.expiresAt) === '#FFD54F')
    : items;

  // Handle selection of items
  const handleSelect = (item) => {
    setSelectedItems((prevSelected) =>
      prevSelected.includes(item)
        ? prevSelected.filter(selectedItem => selectedItem !== item)
        : [...prevSelected, item]
    );
  };

  // Submit selected items
  const handleSubmit = () => {
    const submitData = {
      "store": 1,
      "items": selectedItems
    }
    console.log(submitData);
    axios.post('http://127.0.0.1:8000/backend/api/request/', submitData)
      .then(response => {
        console.log('Data submitted successfully:', response.data);
        // Optionally clear the selected items
        setSelectedItems([]);
      })
      .catch(error => {
        console.error('Error submitting data', error);
      });
  };

  return (
    <Container maxWidth="lg" style={{ marginTop: '20px' }}>
      <Typography variant="h4" gutterBottom>
        Items List
      </Typography>

      <Grid container spacing={2} style={{ marginBottom: '20px' }} alignItems="center">
        <Grid item xs={12} sm={6} md={3}>
          <TextField
            label="Today"
            type="date"
            fullWidth
            InputLabelProps={{
              shrink: true,
            }}
            value={today}
            onChange={(e) => setToday(e.target.value)}
            InputProps={{
              style: { backgroundColor: 'white' } // Ensure background is white
            }}
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <TextField
            label="Upcycle Buffer (days)"
            type="number"
            fullWidth
            value={upcycleBuffer}
            onChange={(e) => setUpcycleBuffer(parseInt(e.target.value, 10) || 0)}
            inputProps={{ min: 0 }}
            InputProps={{
              style: { backgroundColor: 'white' } // Ensure background is white
            }}
          />
        </Grid>
        <Grid item xs={12} sm={12} md={6}>
          <Button
            variant="contained"
            color="primary"
            onClick={() => setFilterUpscale(!filterUpscale)}
            style={{ width: '100%' }} // Ensure button takes full width in its grid cell
          >
            {filterUpscale ? 'Show All' : 'Filter Upscale'}
          </Button>
        </Grid>
      </Grid>

      <Grid container spacing={4}>
        {filteredItems.map((item, index) => (
          <Grid item xs={12} sm={6} md={4} lg={3} key={index} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <Card style={{ 
              backgroundColor: getBackgroundColor(item.expiresAt),
              color: getBackgroundColor(item.expiresAt) === '#F44336' ? 'white' : 'black',
              minWidth: '250px', // Ensure a minimum width for cards
              position: 'relative', // Position relative for checkmark
              paddingBottom: '80px' // Extra space for button at the bottom
            }}>
              {getBackgroundColor(item.expiresAt) === '#FFD54F' && (
                <Checkbox
                  checked={selectedItems.includes(item)}
                  onChange={() => handleSelect(item)}
                  style={{ position: 'absolute', top: 10, right: 10 }}
                />
              )}
              <CardHeader
                avatar={
                  <Avatar>
                    <InventoryIcon />
                  </Avatar>
                }
                title={item.name}
                subheader={`Available: ${item.available}`}
              />
              <CardContent>
                <Typography variant="body2" color="textSecondary">
                  Expiration Date: {new Date(item.expiresAt).toLocaleDateString()}
                </Typography>
                <Typography variant="body2" color="textSecondary">
                  Weight: {item.weight}
                </Typography>
              </CardContent>
              {getBackgroundColor(item.expiresAt) === '#FFD54F' && (
                <Button
                  variant="contained"
                  color="primary"
                  onClick={() => handleSelect(item)}
                  style={{ position: 'absolute', bottom: 10, left: '50%', transform: 'translateX(-50%)', width: '90%' }}
                >
                  Select
                </Button>
              )}
            </Card>
          </Grid>
        ))}
      </Grid>

      {selectedItems.length > 0 && (
        <Button
          variant="contained"
          color="secondary"
          onClick={handleSubmit}
          style={{ marginTop: '20px', width: '100%' }}
        >
          Submit Selected Items
        </Button>
      )}
    </Container>
  );
};

export default ItemList;
