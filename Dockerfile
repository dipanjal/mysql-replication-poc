FROM amazoncorretto:11

ARG JAR_FILE=./sbtest-app/target/*.jar
ARG APP_DIR=/opt/app

COPY ${JAR_FILE} ${APP_DIR}/application.jar
WORKDIR ${APP_DIR}
ENTRYPOINT ["java", "-Dspring.profiles.active=${ACTIVE_PROFILE}", "-jar", "application.jar"]