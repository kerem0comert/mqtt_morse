```

```

# Morse MQTT

The objective is to facilitate communcitation in Morse code between two clients through the MQTT protocol.

# Usage

## Subscribe
Subscribe to incoming messages via running:
```
python subscribe.py
```

## Publish
The letters are seperated via a space character. There is no word seperation. 
e.g. ". -" corresponds to ET.

As such, to publish a message run **publish.py** via:
```
python publish.py -m "[YOUR MSG]"
```
