function EventTimeline() {
  return (
    <div>
      <h3>Major Oil Market Events</h3>
      <p>
        This component presents a timeline of major geopolitical and economic
        events affecting the oil market, such as wars, OPEC decisions, and
        economic crises.
      </p>
      <p>
        Events are retrieved from the backend API endpoint
        <code> /api/events</code> and are used to contextualize detected change
        points.
      </p>
    </div>
  );
}

export default EventTimeline;
