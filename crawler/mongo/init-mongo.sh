mongo -- "$MONGO_INITDB_DATABASE" << EOF
    db.createCollection('$MONGO_COLLECTION');
    db.$MONGO_COLLECTION.createIndex({id: 1}, unique=true);
EOF

if [ "$MODE" = "production" ]; then
    mongo -- "$MONGO_INITDB_DATABASE" "db.createUser({user: '$MONGO_PROD_USERNAME',
        pwd: '$MONGO_PROD_PASSWORD', roles: [{role: 'readWrite', db: '$MONGO_INITDB_DATABASE'}]);"
fi
