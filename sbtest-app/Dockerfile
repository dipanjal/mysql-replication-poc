# Build stage
FROM maven:3.9.6-eclipse-temurin-11 AS build
COPY ./src /home/app/src
COPY ./pom.xml /home/app
RUN mvn -f /home/app/pom.xml clean package -DskipTests=true

# Packaging and Run the staged build
FROM eclipse-temurin:11-jre-alpine
ARG APP_DIR=/opt/app
COPY --from=build /home/app/target/*.jar ${APP_DIR}/app.jar
EXPOSE 8080
# WORKDIR /usr/local/lib
WORKDIR ${APP_DIR}
ENTRYPOINT ["java", "-Dspring.profiles.active=${ACTIVE_PROFILE:default}", "-jar", "app.jar"]
